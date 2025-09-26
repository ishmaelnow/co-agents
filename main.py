from graph import app
from state import SecretaryState  # ✅ Import your state class

task = input("Enter the company task: ")
raw_state = app.invoke({"task": task})

# ✅ Coerce dict to SecretaryState
final_state = SecretaryState(**raw_state)

print("\n🌐 Search Result:\n", final_state.search_result)
print("\n🧠 Search Reflection:\n", final_state.search_reflection)
print("\n🌤️ Weather:\n", final_state.weather)
print("\n📄 Final Letter:\n", final_state.letter)
print("\n🪞 Reflection:\n", final_state.reflection)
print("\n📅 Timestamp:\n", final_state.timestamp)
print("\n🧪 Evaluation:\n", final_state.evaluation)
print("\n🧼 Formatted Letter:\n", final_state.formatted_letter)
print("\n📤 Notification:\n", final_state.notification or "No delivery status available.")