import subprocess
from pprint import pprint
import json
def give_general_information_of_system(do_you_want_to_check_the_installation_is_proper):
    result = subprocess.run(
        ["pip", "install", "batman-ai-toolkit"],
        capture_output=True,
        text=True
    )
    if do_you_want_to_check_the_installation_is_proper:
        print(result)
    result = subprocess.run(
        ["batman-batarang", "analyze"],
        capture_output=True,
        text=True
    )

    return json.loads(result.stdout)

# if __name__=="__main__":
#     do_you_want_to_check_the_installation_is_proper = True
#     result = give_general_information_of_system(do_you_want_to_check_the_installation_is_proper)
#     pprint(result)
