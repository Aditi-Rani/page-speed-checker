import requests
import time

def check_page_speed(url):
    try:
        print(f"\n⏳ Checking speed for: {url}")
        start = time.time()
        response = requests.get(url, timeout=10)
        end = time.time()

        load_time = round(end - start, 2)

        print(f"✅ Status Code: {response.status_code}")
        print(f"⚡ Page Load Time: {load_time} seconds")

        if load_time < 1:
            print("🚀 Excellent speed!")
        elif load_time < 3:
            print("👍 Good speed, consider optimization.")
        else:
            print("🐢 Slow speed! Improve page performance (optimize images, reduce JS, enable caching, etc.)")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")

if __name__ == "__main__":
    url = input("Enter the website URL (include https://): ").strip()
    check_page_speed(url)
