import re
new_id = "...!@BaT#*..y.abcdefghijklm"

def solution(new_id):
    new_id = new_id.lower()

    new_id = "".join(re.findall("[a-z0-9\.\-\_]", new_id))
    # new_id = re.sub("[^a-z0-9\.\-\_]","",new_id)
    
    new_id = re.sub("\.+\.", ".", new_id)

    new_id = new_id.strip(".")

    if not new_id:
        new_id = "a"
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
    # 'a' if len(st) == 0 else st[:15]
    new_id = new_id.strip(".")

    if len(new_id) <= 2:
        new_id = new_id + str(new_id[-1]*(3-len(new_id)))

    answer = new_id
    return answer

solution(new_id)