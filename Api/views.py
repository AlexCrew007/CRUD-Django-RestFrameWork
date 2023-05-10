from rest_framework.response import Response
from rest_framework import status, generics
from Api.models import BooksApiModel
from Api.serializers import ApiSerializer
import math
from datetime import datetime


class BooksApi(generics.GenericAPIView):
    serializer_class = ApiSerializer
    queryset = BooksApiModel.objects.all()

    def get(self, request):
        isbn = int(request.GET.get("isbn",-1))
        if isbn == -1:
            books = BooksApiModel.objects.all()
        else:
            books = BooksApiModel.objects.filter(isbn=isbn)
        serializer = self.serializer_class(books, many=True)
        return Response({
            "status": "success",
            "data" : serializer.data
            
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    


class BooksApi2(generics.GenericAPIView):
    serializer_class = ApiSerializer
    queryset = BooksApiModel.objects.all()
    def get_note(self, pk):
        try:
            return BooksApiModel.objects.get(isbn=pk)
        except:
            return None
    def patch(self, request, pk):
        book = self.get_note(pk)
        if book == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        print(request.data)
        print(book.title)
        serializer = self.serializer_class(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        book = self.get_note(pk)
        if book == None:
            return Response({"status": "fail", "message": f"Note with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({"status": "sucess", "message": f"Note with Id: {pk} deleted"}, status=status.HTTP_404_NOT_FOUND)
