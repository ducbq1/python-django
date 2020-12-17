
import sqlite3
from sqlite3 import Error
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
# from .models import CoAuthorship, PotentialCoAuthor
# from polls.query_database import select_co_author

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def processdatabase(request):

    
    quantityRecord = request.POST['quantityRecord']
    optionProject = request.POST['optionProject']

    if optionProject == "Co-Author":
        records = CoAuthorship.objects.raw("select * from co_author limit " + str(quantityRecord))
        # records = get_object_or_404(CoAuthorship)
        # conn = create_connection(r"../db.sqlite3")
        # c = conn.cursor()
        # c.execute("SELECT * FROM polls_potentialcoauthor")
        # records = c.fetchall()

    elif optionProject == "Co-Author-Potential":
        records = PotentialCoAuthor.objects.raw("select * from potential-co-author limit " + str(quantityRecord))
        # records = select_co_author("select * from polls_potentialcoauthor")

    # return HttpResponseRedirect(reverse('polls:processdatabase', args=(records,)))
    return render(request, 'polls/processdatabase.html', { 'records': records })






def index(request):
    return render(request, 'polls/index.html')


if __name__ == '__main__':
    conn = create_connection(r"../db.sqlite3")
    c = conn.cursor()
    c.execute("SELECT * FROM co_author")
    print(c.fetchall())




# def processdatabase(request):
#     if request.method == 'POST' and request.FILES['databaseName']:
#         databaseName = request.FILES['databaseName']
#         fs = FileSystemStorage()
#         # databaseName = fs.save(databaseName.name, databaseName)
#         uploaded_file_url = fs.url(databaseName)
#         quantityRecord = request.POST['quantityRecord']
#         optionProject = request.POST['optionProject']
#         conn = create_connection(r"../db.sqlite3")
#         c = conn.cursor()

#         if (optionProject == "Co-Author"):

#             # c.execute('''create table co_author as
#             #         select pa1.paper_id,
#             #         pa1.author_id as id_author_1,
#             #         pa2.author_id as id_author_2
#             #         from collab_paper_authors pa1
#             #         join collab_paper_authors pa2
#             #         on pa1.paper_id = pa2.paper_id
#             #         and pa1.author_id < pa2.author_id
#             #         order by pa1.paper_id''')
#             # c.commit()
#             c.execute("select * from django_session order by random() limit 5;")
#             records = c.fetchall()

#         else:

#             c.execute("""
#                     create table potential_co_author as (
#                     select co1.id_author_2 as id_author_1, co2.id_author_2 as id_author_2                    
#                     from co_author co1
#                     join co_author co2
#                     on co1.id_author_1 = co2.id_author_1
#                     and co1.id_author_2 < co2.id_author_2

#                     union

#                     select co2.id_author_1 a
#                     from co_author co1
#                     join co_author co2
#                     on co1.id_author_1 = co2.id_author_2
#                     and co1.id_author_2 > co2.id_author_1

#                     union

#                     select co1.id_author_1 as id_author_1, co2.id_author_2 as id_author_2
#                     from co_author co1
#                     join co_author co2
#                     on co1.id_author_2 = co2.id_author_2
#                     and co1.id_author_1 < co2.id_author_1

#                     union

#                     select co.id_author_1 as id_author_1, co.id_author_2 as id_author_2
#                     from co_author co
#                     )
#                       """)
#             c.commit()
#             c.execute(
#                 "select * from potential_co_author order by random() limit 4")
#             records = c.fetchall()
#             c.close()

#     return HttpResponseRedirect(reverse('polls:processdatabase', args=(records, uploaded_file_url,)))
