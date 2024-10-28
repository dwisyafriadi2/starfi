import requests
import json
import webbrowser

def read_auth_from_file(filename):
    """Read multiple authorization details from a file."""
    with open(filename, 'r') as file:
        auth_tokens = [line.strip() for line in file if line.strip()]
    return auth_tokens

def get_tasks(auth):
    """Fetch the list of tasks from the API."""
    url = 'https://api.stars-fi.com/api/tasks/list'
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'auth': auth,
        'origin': 'https://front.stars-fi.com',
        'priority': 'u=1, i',
        'referer': 'https://front.stars-fi.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch tasks:', response.status_code, response.text)
        return None

def complete_task(auth, task_id):
    """Complete a specific task by ID."""
    url = 'https://api.stars-fi.com/api/tasks/complete'
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'auth': auth,
        'content-type': 'application/json',
        'origin': 'https://front.stars-fi.com',
        'priority': 'u=1, i',
        'referer': 'https://front.stars-fi.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    }

    payload = json.dumps({"id": task_id})
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        result = response.json()
        if 'user' in result and 'stars' in result['user']:
            print('Task completed. Stars earned:', result['user']['stars'])
            print('=========================')
            print('Join Telegram Channel @dasarpemulung or https://t.me/dasarpemulung')
        else:
            print('Task completed, but "stars" information is missing in the response:', result)
    else:
        print('Failed to complete task:', response.status_code, response.text)

def get_sponsor_tasks(auth):
    """Fetch the list of sponsor tasks from the API."""
    url = 'https://api.stars-fi.com/api/sponsors'
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'auth': auth,
        'origin': 'https://front.stars-fi.com',
        'priority': 'u=1, i',
        'referer': 'https://front.stars-fi.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch sponsor tasks:', response.status_code, response.text)
        return None

def complete_sponsor_task(auth, task_id):
    """Complete a specific sponsor task by ID."""
    url = 'https://api.stars-fi.com/api/sponsors/complete'
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'auth': auth,
        'content-type': 'application/json',
        'origin': 'https://front.stars-fi.com',
        'priority': 'u=1, i',
        'referer': 'https://front.stars-fi.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    }

    payload = json.dumps({"id": task_id})
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        result = response.json()
        if 'user' in result and 'stars' in result['user']:
            print('Sponsor task completed. Stars earned:', result['user']['stars'])
        else:
            print('Sponsor task completed, but "stars" information is missing in the response:', result)
    else:
        print('Failed to complete sponsor task:', response.status_code, response.text)

def get_latest_tasks(auth):
    """Fetch the list of latest tasks from the API."""
    url = 'https://api.stars-fi.com/api/earns/latest'
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'auth': auth,
        'origin': 'https://front.stars-fi.com',
        'priority': 'u=1, i',
        'referer': 'https://front.stars-fi.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to fetch latest tasks:', response.status_code, response.text)
        return None

def complete_latest_task(auth, task_id):
    """Complete a specific latest task by ID."""
    url = 'https://api.stars-fi.com/api/earns/complete'
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'auth': auth,
        'content-type': 'application/json',
        'origin': 'https://front.stars-fi.com',
        'priority': 'u=1, i',
        'referer': 'https://front.stars-fi.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    }

    payload = json.dumps({"id": task_id})
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        result = response.json()
        if 'user' in result and 'stars' in result['user']:
            print('Latest task completed. Stars earned:', result['user']['stars'])
        else:
            print('Latest task completed, but "stars" information is missing in the response:', result)
    else:
        print('Failed to complete latest task:', response.status_code, response.text)

def auto_spin(auth):
    """Auto-spin until tickets run out."""
    url = 'https://api.stars-fi.com/api/earns/spin'
    headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9',
        'auth': auth,
        'origin': 'https://front.stars-fi.com',
        'priority': 'u=1, i',
        'referer': 'https://front.stars-fi.com/',
        'sec-ch-ua': '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99", "Microsoft Edge WebView2";v="130"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
    }

    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            if result.get("success"):
                user_info = result.get("user", {})
                tickets = user_info.get("tickets", 0)
                spin_award = result.get("spinAward", 0)
                
                print(f"Spin completed. Award: {spin_award} stars, Tickets left: {tickets}")
                
                if tickets <= 0:
                    print("No tickets left. Stopping auto-spin.")
                    break
            else:
                print("Spin failed:", result)
                break
        else:
            print('Failed to spin:', response.status_code, response.text)
            break



def main():
    auth_tokens = read_auth_from_file('query.txt')  # Read multiple auth tokens

    # Process each authorization token separately
    for auth in auth_tokens:
        print(f"\nProcessing tasks for auth token: {auth}")
        print('=========================')
        print('Join Telegram Channel @dasarpemulung or https://t.me/dasarpemulung')

        # Fetch and complete standard tasks
        tasks = get_tasks(auth)
        if tasks:
            for task in tasks:
                if 'id' in task and 'value' in task and task['value']:
                    webbrowser.open(task['value'])
                complete_task(auth, task['id'])

        # Fetch and complete sponsor tasks
        sponsor_tasks = get_sponsor_tasks(auth)
        if sponsor_tasks:
            for sponsor_task in sponsor_tasks:
                if 'id' in sponsor_task and 'value' in sponsor_task and sponsor_task['value']:
                    webbrowser.open(sponsor_task['value'])
                complete_sponsor_task(auth, sponsor_task['id'])

        # Fetch and complete latest tasks
        latest_tasks = get_latest_tasks(auth)
        if latest_tasks:
            for latest_task in latest_tasks:
                if 'id' in latest_task and 'value' in latest_task and latest_task['value']:
                    webbrowser.open(latest_task['value'])
                complete_latest_task(auth, latest_task['id'])
                
        auto_spin(auth)

        # Fetch and complete standard tasks
        tasks = get_tasks(auth)
        if tasks:
            for task in tasks:
                if 'id' in task and 'value' in task and task['value']:
                    webbrowser.open(task['value'])
                complete_task(auth, task['id'])

if __name__ == "__main__":
    main()
