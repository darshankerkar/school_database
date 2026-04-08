from .models import Professor as ProfessorModel # rename model since same names for classes
from .serializers import ProfessorSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProfessorFilter

# class Professor(APIView):
#     def get(self, request):
#         professors=ProfessorModel.objects.all()
#         serializer=ProfessorSerializer(professors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self, request):
#         serializer=ProfessorSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class ProfessorDetails(APIView):
#     def get_object(self, id): # returns object for the primary key mentioned
#         try:
#             return ProfessorModel.objects.get(id=id) # maintains DRY priciple, otherwise everywhere we need to use try except blocks
#         except ProfessorModel.DoesNotExist:
#             raise Http404
        
#     def get(self, request, id):
#         employee=self.get_object(id) # function call with id as parameter
#         serializer=ProfessorSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, id):
#         employee=self.get_object(id) 
#         serializer=ProfessorSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         employee=self.get_object(id)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# using mixins
"""
class Professor(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset=ProfessorModel.objects.all()
    serializer_class=ProfessorSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class ProfessorDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset=ProfessorModel.objects.all()
    serializer_class=ProfessorSerializer
    lookup_url_kwarg='id'

    def put(self, request, id):
        return self.update(request, id=id)
    
    def get(self, request, id):
        return self.retrieve(request, id=id)
    
    def delete(self, request, id):
        return self.destroy(request, id=id)
"""

# using generics
'''
class Professor(generics.ListCreateAPIView):
    queryset=ProfessorModel.objects.all()
    serializer_class=ProfessorSerializer

class ProfessorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ProfessorModel.objects.all()
    serializer_class=ProfessorSerializer
    lookup_field='id'
'''

# using viewSets
"""
class ProfessorViewSet(viewsets.ViewSet):
    def list(self, request):
        professors=ProfessorModel.objects.all()
        serializer=ProfessorSerializer(professors, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer=ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self, request, pk=None): # see why
        professor = get_object_or_404(ProfessorModel, id=pk) # remember to use get_object_or_404
        serializer=ProfessorSerializer(professor)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        professor = get_object_or_404(ProfessorModel, id=pk)
        serializer=ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        professor = get_object_or_404(ProfessorModel, id=pk)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

from _school_project_root.pagination import MyPagination

# using ModelViewSet
class ProfessorViewSet(viewsets.ModelViewSet):
    queryset=ProfessorModel.objects.all()
    serializer_class=ProfessorSerializer
    pagination_class=MyPagination

    filter_backends=[DjangoFilterBackend]
    filterset_class = ProfessorFilter
