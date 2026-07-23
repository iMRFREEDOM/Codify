from django.http import HttpResponse

# 1. Kitoblar ro'yxati sahifasi
def book_list(request):
    html = """
    <h1>Kitoblar ro'yxati</h1>
    <h2>O'qish uchun kitobni tanlang:</h2>
    <a href="book/garri_potter/">1. Garri Potter >></a> <br><br>
    <a href="book/bizning_shahrimizda/">2. Bizning shahrimizda o'g'ri yo'q >></a>
    """
    return HttpResponse(html)

def book_detail(request, book):
    if book == "garri_potter":
        html = """
        <h1>Garri Potter</h1>
        <p>
        Harry Potter discovers he is a wizard, attends Hogwarts, and faces challenges with friends Ron and Hermione.
        Across adventures, he battles Lord Voldemort, learning about courage, friendship, and sacrifice.
        </p>
        <br>
        <a href="../.."> << Ortga (Kitoblar ro'yxatiga qaytish) </a>
        """
    elif book == "bizning_shahrimizda":
        html = """
        <h1>Bizning shahrimizda o'g'ri yo'q</h1>
        <p>
        Gabriel García Márquez portrays a town claiming to be free of thieves.
        Through irony and realism, the story exposes hidden corruption, hypocrisy, and moral contradictions.
        </p>
        <br>
        <a href="../.."> << Ortga (Kitoblar ro'yxatiga qaytish) </a>
        """
    else:
        html = """
        <h1>Bunday kitob topilmadi! </h1>
        <br>
        <a href="../.."> << Ortga </a>
        """
    return HttpResponse(html)