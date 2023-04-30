
PID = int(sys.argv[1])

def print_n(string):
    print(string)
    print(f"Node-{PID}> ",end="")
    return

#------------------ main -------------------#

def main():
    chain_exists = False
    
    print_n("Waiting for command")
    while True:
        command = input()
        args = command.split(" ")

        if args[0].lower() == "local-store-ps":
            k = int(args[1])
            
        elif args[0].lower() == "create-chain":
            if chain_exists:
                print("Warning! A chain already exists. Do you want to re-creating the chain. y/n ")
                command = input().lower()
                if command == "y":
                    # re-creating the chain
                    pass

        elif args[0].lower() == "list-chain":
            # list the current status of the chain
            pass

        elif args[0].lower() == "write-operation":
            data = args[1].split(", ")
            name = data[0].strip("<").strip("\"")
            price = float(data[1].strip(">"))

        elif args[0].lower() == "list-books":
            # lists the available books in the store
            pass

        elif args[0].lower() == "read-operation":
            name = args[1].strip("\"")

        elif args[0].lower() == "time-out":
            time = int(args[1])

        elif args[0].lower() == "data-status":
            # list the status of each data item
            pass

        elif args[0].lower() == "remove-head":
            # remove the current head from the chain
            pass

        elif args[0].lower() == "restore-head":
            # restore the most recent removed head back to chain
            pass

        else:
            print_n("Command not found")


if __name__ == "__main__":
    main()