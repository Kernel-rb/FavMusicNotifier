# 🎵 FavMusicNotifier

## Description
FavMusicNotifier is a Python script that enhances your music listening experience. Play your favorite playlist seamlessly, receive email notifications for errors during playback, and enjoy animated displays to add a visual touch to your music sessions.

## Features
- Seamless playback of your favorite music playlist.
- Email notifications for errors during music playback.
- Engaging animated display during music sessions.

## Usage
1. Ensure you have Python installed on your system.
2. Edit the `config.ini` file with your email credentials.
3. Run the `main.py` script to start playing your playlist.
4. Enjoy an immersive music experience with visual animations.

## 📂 Directory Structure
/: 
  .venv/
  playlist/
  config.ini
  main.py
  test_smtp.py

## Dependencies
- Python 3.x
- Keyboard library (`pip install keyboard`)

## 🛠 Configuration
Edit the `config.ini` file with your email credentials:

[Email]
sender_email = your_sender_email@gmail.com
receiver_email = your_receiver_email@gmail.com
password = your_email_password

**Note:**
- Ensure to enable "Less secure app access" in your Google account settings.
- The script uses the keyboard library for shortcut handling.

## Author
[Your Name]

## License
This project is licensed under the [MIT License](LICENSE).
