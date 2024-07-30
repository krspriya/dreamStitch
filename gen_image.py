import os

U_cookie_api_key_value = '1qrzH2Ny4oXLJHwvjBjMbExX4dHBK1HW6YvNRc2cbLkZbkqkjbolasRo9o6AJNGuDO2E5Q1vRIjFcdNSdBrZ7IVA2MqxbYQqezL5u0l0g5HYsg8BcaaV_E_Fr-Uhs02qUl7ww_wFn9HU_-V9dKzsBuyCuz8s2LU99aGUQm80vZ6nSOnbC9TR97y_j9IuaQnWCcxykxrsnwSJlV7308-oTC09STBDkZV6nK1nItLIbpw8'
def generate_images(prompt):

    command = f'python -m BingImageCreator --prompt "{prompt}" -U "{U_cookie_api_key_value}"'
    os.system(command)

    return os.listdir("OUTPUT")

image_list = generate_images("Design a chic, knee-length dress with a fitted bodice and flared skirt. Incorporate a deep V-neckline with delicate lace trim and cap sleeves.Use a luxurious navy blue satin fabric with a subtle sheen. Add a high waistline with a matching sash tied into a bow at the back. Include intricate embroidery along the hemline for an elegant touch.")

