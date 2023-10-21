from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from app1.service.ishchi import Ishchi
from app1.service.format import ishchi_format


# Create your views here.


class Ishchiview(GenericAPIView):
    def get(self, request, pk=None):
        if pk:
            ishchi = Ishchi.objects.filter(id=pk).first()
            if not ishchi:
                ctx = {
                    "Error": "Ishchi not found"
                }
                return Response(ctx)

            ctx = {"Success": ishchi_format(ishchi)}
            return Response(ctx)

        else:
            ishchilar = Ishchi.objects.all()
            bush_list = []
            for i in ishchilar:
                bush_list.append(ishchi_format(i))
            return Response(bush_list)

    def delete(self, request, pk):
        ishchi = Ishchi.objects.filter(id=pk).first()
        if not ishchi:
            return Response({
                "error": "Ishchi yoq"
            })
        else:
            ishchi.delete()
            return Response({"Success": "Success"})
