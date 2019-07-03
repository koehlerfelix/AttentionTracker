import util.pdfConverter as pdfC


class PdfViewer:
    __pdfCon = pdfC.PdfConverter()

    def __init__(self):
        self.__current_page = 0
        self.__pages = []

    def init_file(self, file):
        self.__pages = self.__pdfCon.convert(file)

    def num_of_pages(self):
        return len(self.__pages)

    def get_all_pages(self):
        return self.__pages

    def get_current_page(self):
        return self.get_page(self.__current_page)

    def get_page(self, page_index):
        if self.page_index_valid(page_index):
            return self.__pages[page_index]

    def get_current_page_index(self):
        return self.__current_page

    def get_next_page_index(self):
        if self.page_index_valid(self.__current_page + 1):
            return self.__current_page + 1
        else:
            return 0

    def get_previous_page_index(self):
        if self.page_index_valid(self.__current_page - 1):
            return self.__current_page - 1
        else:
            return len(self.__pages) - 1

    # check if page is within bounds
    def page_index_valid(self, page_index):
        return len(self.__pages) > page_index > -1

    def set_page_index(self, page_index):
        if self.page_index_valid(page_index):
            self.__current_page = page_index
