import os
import sys
from extract_msg import Message

def convert_msg_to_eml(input_folder):
    if not os.path.exists(input_folder):
        print(f"❌ Error: The folder '{input_folder}' does not exist.")
        return

    output_folder = os.path.join(input_folder, "Converted Emails")
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".msg"):
            msg_file = os.path.join(input_folder, file)
            eml_file = os.path.join(output_folder, file.replace(".msg", ".eml"))
            
            try:
                msg = Message(msg_file)
                msg.save(eml_file)
                print(f"✅ Converted: {msg_file} → {eml_file}")
            except Exception as e:
                print(f"❌ Error converting {msg_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: Drag a folder onto the app to convert MSG files to EML.")
        sys.exit(1)

    input_folder = sys.argv[1]
    convert_msg_to_eml(input_folder)
