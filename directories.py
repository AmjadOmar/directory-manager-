class Directory:
    def __init__(self):
        self.directories = {}

    def create(self, path: str):
        parts = path.split('/')
        current = self.directories
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
        print(f"CREATE {path}")

    def move(self, source: str, destination: str):
        source_parts = source.split('/')
        dest_parts = destination.split('/')
        current = self.directories

        # Traverse to the source directory
        for part in source_parts[:-1]:
            current = current.get(part, {})

        # Remove the source directory from its current location
        dir_to_move = current.pop(source_parts[-1], None)

        if dir_to_move is None:
            print(f"Cannot move {source} - {source_parts[-1]} does not exist")
            return

        # Traverse to the destination directory
        current = self.directories
        for part in dest_parts:
            if part not in current:
                current[part] = {}
            current = current[part]

        # Place the directory in the new location
        current[source_parts[-1]] = dir_to_move
        print(f"MOVE {source} {destination}")

    def delete(self, path: str):
        parts = path.split('/')
        current = self.directories

        # Traverse to the parent directory of the target directory
        for part in parts[:-1]:
            if part not in current:
                print(f"Cannot delete {path} - {parts[-2]} does not exist")
                return
            current = current[part]

        # Attempt to delete the directory
        if parts[-1] in current:
            del current[parts[-1]]
            print(f"DELETE {path}")
        else:
            print(f"Cannot delete {path} - {parts[-1]} does not exist")

    def list_directories(self, current=None, indent=0):
        if current is None:
            current = self.directories

        for name in sorted(current):
            print("  " * indent + name)
            self.list_directories(current[name], indent + 1)

def main():
    dir_manager = Directory()

    while True:
        try:
            command = input()
            if command.strip().lower() == "exit":
                print("Exiting...")
                break

            parts = command.split()
            action = parts[0].upper()

            if action == "CREATE":
                dir_manager.create(parts[1])
            elif action == "MOVE":
                dir_manager.move(parts[1], parts[2])
            elif action == "DELETE":
                dir_manager.delete(parts[1])
            elif action == "LIST":
                dir_manager.list_directories()
            else:
                print("Invalid command")
        except (IndexError, ValueError) as e:
            print(f"Error: {e}. Please check the command and try again.")

if __name__ == "__main__":
    main()
