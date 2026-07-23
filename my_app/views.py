from django.http import HttpResponse

def first_view(request):
    html = """
    <h1>First page</h1>
    <h2>Asosiy bo'lim</h2>
    <a href="second/"> second page >> </a> <br>
    <a href="pages/kompyuterlar"> Computers page >> </a><br>
    <a href="pages/telefonlar"> Telephones page >> </a>
    
    """
    return HttpResponse(html)

def second_view(request):
    html = """
    <h1>Second page</h1>
    <h2>Ikkinchi bo'lim</h2>
     <a href="../"> << first page </a>
    """
    return HttpResponse(html)

def third_(request):
    html = """
    <h1>Third page</h1>
    <a href="third/"> Third page >> </a> <br>
    <a href="pages/Bizning_shaxrimizda.."> Computers page >> </a><br>
    <a href="pages/garri_potter"> Computers page >> </a><br>
    """
    return HttpResponse(html)

def pages(request,page):
    if page == "Bizning_shaxrmizda..":
        html = f"""
        <h1>{page}</h1>
        <p>
        Harry Potter  
        Harry Potter discovers he is a wizard, attends Hogwarts, and faces challenges with friends Ron and Hermione. Across adventures, he battles Lord Voldemort, learning about courage, friendship, and sacrifice in a magical world filled with danger and wonder.
        </p>
         <a href="../"> << main page </a>
        """
    elif page == "garri_potter":
        html = f"""
        <h1>{page}</h1>
        <p>Bizning shahrimizda o'g'ri yo'q  
    Gabriel García Márquez portrays a town claiming to be free of thieves. Through irony and realism, the story exposes hidden corruption, hypocrisy, and moral contradictions, questioning whether true justice exists in society or if    a
ppearances mask deeper flaws.
        <a href="../"> << main page </a>
        """
    else:
        html = f"""
        <h1>{page}</h1>
        """
    return HttpResponse(html)

