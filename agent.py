# AI Agent Logic for DhanWapas
def get_recovery_strategy(failure_reason):
    strategies = {
        "bank_timeout": "Retry same method, reassuring tone",
        "insufficient_funds": "Suggest UPI Lite, EMI option",
        "card_declined": "Suggest alternate card, Netbanking"
    }
    return strategies.get(failure_reason, "Generic retry link")

# Gemini prompt used
PROMPT = """
You are a payment recovery agent. 
Failure reason: {reason}
Customer: {name}
Amount: {amount}
Generate a short WhatsApp message (max 25 words) with retry link.
Tone: Helpful, not spammy.
"""
