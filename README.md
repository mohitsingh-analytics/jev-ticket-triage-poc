# Jev ticket triage POC

A tiny Python CLI for learning Jev's typed decisions. Paste a support ticket and Jev returns a team choice and urgency score in one request.

## What you'll learn

- How to send a piece of state (the ticket) to Jev.
- How to define a `Choice` and a `Score` question.
- How to read the typed answer and confidence in Python.

## Run it (Windows PowerShell)

1. Install Python 3.10 or newer.
2. Create an API key in the [TypeSafe console](https://console.typesafe.ai/).
3. In this folder, create and activate a virtual environment, then install the SDK:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

4. Set your key for this terminal session and run the demo:

   ```powershell
   $env:TYPESAFE_API_KEY = "your-api-key"
   python triage.py
   ```

Press Enter at the ticket prompt to use the built-in sample. Or paste a ticket of your own.

## Try changing it

- Add or rename a category in the `Choice` criteria.
- Change the urgency descriptions in `Score`.
- Ask a yes/no question with `Noul` (for example, whether the ticket describes a service outage).
- Compare the returned confidence with the model's selected answer.

The model's output is a signal for this learning demo. The demo does not create tickets or take external actions.
