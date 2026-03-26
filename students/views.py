from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

def home(request):
    return render(request, 'home.html')

@api_view(['GET', 'POST']) # This converts a normal Django function into a DRF API view.
def student_details(request):
    if request.method=='GET':
        students = Student.objects.all() # fetch data from browser
        serializer = StudentSerializer(students, many=True) # Convert Model → JSON directly 
        return Response(serializer.data, status=status.HTTP_200_OK) # return json response for serializer data
    # """
    # This is a QuerySet object
    # [
    #     <Student object (id=1)>,
    #     <Student object (id=2)>
    # ]

    # Serializer converts this to dict via some internal oops code 
    # If model instance is:
    # Student(id=1, name="Darshan", age=18)

    # It becomes:
    # { # serailizer.data
    #     "id": 1,
    #     "name": "Darshan",
    #     "age": 18
    # }
    # """
    elif request.method=='POST':
        serializer = StudentSerializer(data = request.data) # Store user request's data
        if serializer.is_valid(): #check if valid data or not 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors) # to view the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # always return status in api's
    
@api_view(['GET', 'PUT', 'DELETE']) # get single 
def student_detail_view(request, id):
    try:
        student=Student.objects.get(roll_no=id) # since we dont have id field in our Student model
    except Student.DoesNotExist: # remember DoesNotExist exception 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=StudentSerializer(student) #no many param
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=='PUT':
        serializer=StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)