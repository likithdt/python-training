students = []

print("Welcome to Simple Student Database")

while True:
      print("\n1. Add student")
      print("2. View students")
      print("3. Search student")
      print("4. Exit")

      choice = input("Choose option (1-4): ")

      if choice == "1":
          name = input("Name: ")
          age = input("Age: ")
          grade = input("Grade: ")
          marks = input("Marks: ")
          contact = input("Contact: ")
          address = input("Address: ")
          students.append({
              "name": name,
              "age": age,
              "grade": grade,
              "marks": marks,
              "contact": contact,
              "address": address
          })
          print("Student added!")

      elif choice == "2":
          print("\nStudents:")
          for i, s in enumerate(students, 1):
              print(f"{i}. {s['name']} (Age: {s['age']})")

      elif choice == "3":
          name = input("Search name: ")
          found = False
          for s in students:
              if s["name"] == name:
                  print(f"Found: {s}")
                  found = True
          if not found:
              print("Not found")

      elif choice == "4":
          print("wrong choice")
          break

      else:
          print("Invalid choice")
