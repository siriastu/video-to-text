import moviepy.editor as mp
import speech_recognition as sr
import streamlit as st

def video_to_text(video_path):
    # Ekstrak audio dari video
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile("audio.wav", codec='pcm_s16le')

    # Transkripsi audio menjadi teks
    recognizer = sr.Recognizer()

    with sr.AudioFile("audio.wav") as file_audio:
        audio_data = recognizer.record(file_audio)

    try:
        result_text = recognizer.recognize_google(audio_data, language="id-ID")
        return result_text
    except sr.UnknownValueError:
        return "google web Speech API tidak mengenali audio"
    except sr.RequestError as e:
        return f"error on request API: {e}"

# Penggunaan
video_path = st.text_input("D:\S2\AI PROJECT\homework\ganjarp.mp4")
if video_path:
    result_text = video_to_text(video_path)
    st.write("Hasil konversi teks:")
    st.write(result_text)
    with open("hasilteks.txt", "w", encoding="utf-8") as hasil_teks:
        hasil_teks.write(result_text)