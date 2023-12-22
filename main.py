import queue
import time


request_queue = queue.Queue()

def generate_request(number_request):
    for i in range(number_request):
        request_id = request_queue.qsize() + 1
        new_request = f"request {request_id}"
        request_queue.put(new_request)
        print(new_request)
        time.sleep(1)


def process_request():
    while True:
      
        if not request_queue.empty():
            processed_request = request_queue.get()
            print(f"Processing: {processed_request}")
            time.sleep(2)
        else:
            print("No requests to process.")
            break



def main():

    while True:
        number_req = input("Enter a count of queue: ").strip()
        if not number_req.isdigit():  
            print("Queue is empty, exit the program")
            break
        generate_request(int(number_req))
        process_request()

if __name__ == "__main__":
    main()