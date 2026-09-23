import subprocess
from pprint import pprint
import json
def give_general_information_of_system():
    result = subprocess.run(
        ["pip", "install", "batman-ai-toolkit"],
        capture_output=True,
        text=True
    )
    result = subprocess.run(
        ["batman-batarang", "analyze"],
        capture_output=True,
        text=True
    )

    return json.loads(result.stdout)

# if __name__=="__main__":
#     result = give_general_information_of_system()
#     pprint(result)
