from app import path
from views import *
urls = ({
    path('/show_load/', show_load_file),
    path('/upload_file/', upload_file),
    path('/load_file/<filename>/', download_file),

})

