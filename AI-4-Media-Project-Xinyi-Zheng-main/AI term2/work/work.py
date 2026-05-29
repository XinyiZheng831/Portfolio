import cv2
import mediapipe as mp
import numpy as np
import math
import threading
import time
from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import low_pass_filter

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Audio control variables
current_track = 'output.wav'  
current_volume = 1.0
current_pitch = 1.0
current_filter_freq = 1000
current_distortion = 0.0  
running = True
switch_music = False  # Flag for switching music
last_switch_time = 0  # Time of the last music switch

def adjust_volume(distance):
    """Adjust volume based on thumb-index finger distance"""
    return min(max(distance * 10, 0.1), 1.0)

def adjust_pitch(hand_y, frame_height):
    """Adjust pitch based on hand height"""
    normalized_y = hand_y / frame_height
    return min(max(2.0 - (normalized_y * 1.5), 0.5), 2.0)

def adjust_filter_freq(hand_y, frame_height):
    """Adjust filter frequency based on hand height"""
    normalized_y = hand_y / frame_height
    return int(min(max(normalized_y * 2000, 100), 2000))

def apply_distortion(audio_segment, distortion_level):
    """Apply distortion effect"""
    if distortion_level <= 0:
        return audio_segment
    # Distort the audio by increasing volume and clipping the waveform
    distorted_audio = audio_segment + (20 * np.log10(1 + distortion_level * 10))
    return distorted_audio

def play_audio():
    """Play audio and adjust effects based on gestures"""
    global current_volume, current_pitch, current_filter_freq, current_distortion, running, current_track, switch_music

    while running:
        # Load the current music track
        original_audio = AudioSegment.from_wav(current_track)

        while not switch_music and running:
            modified_audio = original_audio._spawn(original_audio.raw_data, overrides={
                "frame_rate": int(original_audio.frame_rate * current_pitch)
            }).set_frame_rate(original_audio.frame_rate)

            # Apply low-pass filter
            modified_audio = low_pass_filter(modified_audio, current_filter_freq)

            # Apply distortion effect
            modified_audio = apply_distortion(modified_audio, current_distortion)

            # Adjust volume
            modified_audio = modified_audio + (20 * np.log10(current_volume) if current_volume > 0 else -100)

            play(modified_audio)

        # Switch music track
        if switch_music:
            if current_track == 'output.wav':
                current_track = 'output2.wav'
            elif current_track == 'output2.wav':
                current_track = 'output3.wav'
            else:
                current_track = 'output.wav'
            switch_music = False
            print(f"Switched to next track: {current_track}")

audio_thread = threading.Thread(target=play_audio, daemon=True)
audio_thread.start()

# Visual parameters
size = 30
num_shapes = 8
rotation_angle = 0
alpha = 1
center = (950, 550)
num_sub_circles = 5
time_factor = 0
particles = []

# Color control
def get_black_or_white_color(t):
    return (255, 255, 255) if int(t) % 2 == 0 else (0, 0, 0)

def create_gradient_background(width, height):
    """Create a black-and-white gradient background"""
    gradient = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height):
        color = int(255 * (i / height))
        gradient[i, :] = [color, color, color]
    return gradient

def draw_dynamic_shapes(img, size, rotation, color, alpha, time_factor, num_sub, line_scale):
    """Draw complex black-and-white visual effects, including lines and circles"""
    for i in range(num_shapes):
        angle = 2 * math.pi * i / num_shapes + rotation
        x = int(center[0] + 200 * math.cos(angle))
        y = int(center[1] + 200 * math.sin(angle))

        overlay = img.copy()
        cv2.circle(overlay, (x, y), size, color, -1)

        for j in range(num_sub):
            sub_angle = 2 * math.pi * j / num_sub + time_factor * 0.05
            sub_x = int(x + size * 2 * math.cos(sub_angle))
            sub_y = int(y + size * 2 * math.sin(sub_angle))
            cv2.circle(overlay, (sub_x, sub_y), max(5, size // 3), color, -1)

        cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

        for j in range(num_shapes):
            end_angle = 2 * math.pi * j / num_shapes + rotation
            end_x = int(center[0] + 250 * line_scale * math.cos(end_angle))
            end_y = int(center[1] + 250 * line_scale * math.sin(end_angle))
            cv2.line(img, (x, y), (end_x, end_y), color, 1)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Unable to access camera")
    running = False
    exit()

def is_hands_praying(hand_landmarks_list):
    """Detect if hands are clasped together (praying gesture)"""
    if len(hand_landmarks_list) != 2:  # Requires two hands
        return False

    # Get the palm positions of both hands
    palm1 = hand_landmarks_list[0].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
    palm2 = hand_landmarks_list[1].landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]

    # Calculate the distance between the palms
    distance = math.sqrt((palm1.x - palm2.x) ** 2 + (palm1.y - palm2.y) ** 2)

    # If the distance is below a threshold, consider the hands clasped
    return distance < 0.08  # Adjust threshold for better detection

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Unable to read frame")
        break

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    background = create_gradient_background(image.shape[1], image.shape[0])
    color = (255, 255, 255)
    num_sub_circles = 5
    line_scale = 1.0  # Default line scaling factor

    if results.multi_hand_landmarks:
        hand_landmarks_list = results.multi_hand_landmarks

        for hand_landmarks in hand_landmarks_list:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            distance = math.sqrt((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2)

            if wrist.x < 0.5:  # Left hand controls visuals
                size = int(min(max(10 + distance * 400, 10), 150))

                if pinky_tip.y < index_tip.y:
                    rotation_angle += 0.3

                if thumb_tip.y < index_tip.y:
                    color = (255, 0, 255)
                else:
                    color = get_black_or_white_color(time_factor * 0.1)

                alpha = max(0.3, min(1.0, 1 - abs(pinky_tip.x - index_tip.x) * 5))

                num_sub_circles = int(min(max(3 + distance * 20, 3), 8))

                particles.append((int(index_tip.x * frame_width), int(index_tip.y * frame_height), 0))

                # Adjust line scaling based on gesture distance
                line_scale = min(max(distance * 2, 0.5), 2.0)

            elif wrist.x > 0.5:  # Right hand controls audio
                current_volume = adjust_volume(distance)
                palm_y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y * frame_height
                current_pitch = adjust_pitch(palm_y, frame_height)
                current_filter_freq = adjust_filter_freq(palm_y, frame_height)

                # Calculate the movement of three fingers
                finger_tips = [index_tip, middle_tip, ring_tip]
                finger_heights = [tip.y for tip in finger_tips]
                avg_height = np.mean(finger_heights)
                current_distortion = abs(avg_height - 0.5) * 2  # Normalize to 0-1 range

                print(f"Current Volume: {current_volume * 100:.1f}%, Current Pitch: {current_pitch:.2f}x, Current Filter Freq: {current_filter_freq}Hz, Current Distortion: {current_distortion:.2f}")

        # Detect praying hands gesture
        if is_hands_praying(hand_landmarks_list):
            current_time = time.time()
            if current_time - last_switch_time > 2:  # Wait at least 2 seconds 
                switch_music = True
                last_switch_time = current_time  # Update 

    time_factor += 1

    final_image = background.copy()
    draw_dynamic_shapes(final_image, size, rotation_angle, color, alpha, time_factor, num_sub_circles, line_scale)

    for i, (px, py, age) in enumerate(particles):
        cv2.circle(final_image, (px, py), max(1, 10 - age), (0, 0, 255), -1)
        particles[i] = (px, py, age + 1)
        
    # Display real-time parameters in the top-left corner
    cv2.putText(final_image, f"Volume: {current_volume:.2f}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(final_image, f"Pitch: {current_pitch:.2f}", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(final_image, f"Filter: {current_filter_freq} Hz", (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(final_image, f"Distortion: {current_distortion:.2f}", (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(final_image, f"Track: {current_track}", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(final_image, "Clasp hands to switch music", (20, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    user_image_resized = cv2.resize(frame, (320, 240))
    final_image[-240:, -320:] = user_image_resized

    cv2.imshow("Hand Gesture Visual & Audio Control", final_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        running = False
        break

cap.release()
cv2.destroyAllWindows()