class MeditationApp:
    def __init__(self):
        self.sessions = []

    def add_session(self, duration, description):
        self.sessions.append({"Duration": duration, "Description": description})

    def view_sessions(self):
        print("Evening Meditation Sessions:")
        for i, session in enumerate(self.sessions, 1):
            print(f"Session {i}: {session['Duration']} minutes - {session['Description']}")

app = MeditationApp()
app.add_session(10, "Breathing exercises")
app.add_session(20, "Guided visualization")
app.view_sessions()
