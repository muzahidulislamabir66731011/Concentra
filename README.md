# Concentra - Study and Focus Voice Assistant

Concentra is a simple voice-controlled assistant designed to help you stay focused during study or work sessions.  
You just speak the number of minutes to set a timer, and Concentra will alert you when time is up.

---

## Features

- Voice input for setting an alarm timer in minutes  
- Speech feedback confirming your input  
- Alerts when your focus session ends

---

## How to Use

1. Run the program.  
2. Listen to Concentra’s greeting and instructions.  
3. Say the alarm time in minutes (e.g., "25").  
4. Wait until the alarm sounds.

---

## Dependencies

This project requires the following Python packages:

- `gtts` — Google Text-to-Speech, converts text to spoken audio  
- `pygame` — Plays the audio output  
- `speech_recognition` — Captures and recognizes your voice input  
- `word2number` — Converts spoken numbers (words) to numeric values

Install all dependencies with:

```bash
pip install gtts pygame SpeechRecognition word2number

License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).
You can use, share, and modify this project for non-commercial purposes only. See the LICENSE file for details.
Notes

    Make sure your microphone is set up and working correctly.

    Background noise may affect speech recognition accuracy.

    Requires an internet connection for Google speech services.

Feel free to contribute or suggest improvements!
