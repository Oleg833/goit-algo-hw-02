import queue
import time
import uuid

request_queue = queue.Queue()

def generate_request():
    request_id = str(uuid.uuid4())
    new_request = f"request {request_id}"
    request_queue.put(new_request)
    print( f"\nNew request: {request_id}")
    time.sleep(1)

def process_request():
    if not request_queue.empty():
        processed_request = request_queue.get()
        print(f"\nProcessing...{processed_request}")
        time.sleep(2)
    else:
        print("\nNo requests to process.")


def main():

    try:
        while True:
            generate_request()
            
            process_request()            

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()