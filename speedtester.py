import tkinter as tk
from tkinter import messagebox
import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

    return download_speed, upload_speed

def display_speeds():
    download_speed, upload_speed = test_internet_speed()
    messagebox.showinfo("Speed Test Results", f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps")

def main():
    root = tk.Tk()
    root.title("Internet Speed Tester")

    label = tk.Label(root, text="Click the button to test internet speed:")
    label.pack(pady=10)

    test_button = tk.Button(root, text="Test Speed", command=display_speeds)
    test_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
