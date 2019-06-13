class PdfViewer:
    __current_page = 0
    __pages = []

    def get_all_pages(self):
        return self.__pages

    def get_single_page(self, page):
        if page < 0 or page > len(self.__pages):
            return
        return self.__pages[page]

    def get_next_page(self):
        if len(self.__pages) == self.__current_page:
            self.__current_page = 0
        self.__current_page += 1
        return self.__pages

    def set_pages(self, pages):
        self.__pages = pages
