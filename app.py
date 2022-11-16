import os

from flask import Flask, jsonify, request
from PyPDF2 import PdfFileReader, PdfFileWriter

app = Flask(__name__)

RESULT_DUMP_PATH = os.path.join(os.getcwd(), "res")


@app.route("/pdf-rotate", methods=["POST"])
def pdf_rotate() -> str:
    """
    :purpose:rotate the specified page and keep other pages intact
    :param: pdf: path to the pdf file
    :param: page_no: page number to rotate
    :param: angle: angle to rotate
    :return: path to the rotated pdf file
    """
    # get the params from the request
    file_path, page_number, rotation_angle = (
        request.json["file_path"],
        request.json["page_number"],
        request.json["rotation_angle"],
    )
    if rotation_angle % 90 != 0:
        return jsonify({"error": "rotation angle must be a multiple of 90"}), 400
    # validate existence of the file
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 400
    # read file and rotate the specified page number
    try:
        pdf = PdfFileReader(file_path)
        page = pdf.getPage(page_number)
    except IndexError:
        return jsonify({"error": "Page number out of range"}), 400
    page.rotateClockwise(rotation_angle)
    writer = PdfFileWriter()
    writer.append_pages_from_reader(pdf)
    if not os.path.exists(RESULT_DUMP_PATH):
        os.makedirs(RESULT_DUMP_PATH)
    # write the rotated pdf to the result folder
    with open(os.path.join(RESULT_DUMP_PATH, "rotated.pdf"), "wb") as f:
        writer.write(f)
    return (
        jsonify(
            {
                "success": "File rotated successfully",
                "path": f"{RESULT_DUMP_PATH}/rotated.pdf",
            }
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)
