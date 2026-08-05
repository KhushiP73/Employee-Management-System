from database import get_connection

def main():
    try:
        conn = get_connection()
        print("Connected to PostgreSQL successfully!")
        conn.close()

    except Exception as e:
        print("Connection Failed!")
        print(e)

if __name__ == "__main__":
    main()