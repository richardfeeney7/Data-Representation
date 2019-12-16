from studentDAO import studentDAO

# Test create
latestid = studentDAO.create(("Mark", 46))
print(latestid)

# Test find by id
result = studentDAO.findByID(latestid)
print(result)
print("----")

# Test update
studentDAO.update(("Rob", 6, latestid))
result = studentDAO.findByID(latestid)
print(result)
print("----")

# Test get all
allStudents = studentDAO.getAll()
for student in allStudents:
    print(student)

# Test delete
print("Want to delete row with id:", latestid)
studentDAO.delete(latestid)