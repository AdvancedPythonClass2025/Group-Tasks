 file.write(f"{datetime.datetime.now()} - تابع '{func.__name__}' اجرا شد\n")
            return result
        return wrapper