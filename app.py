from flask import Flask, redirect, request, url_for, Response, render_template

import images

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return redirect(url_for('api'))


@app.route("/api/", methods=['GET'])
def api():
    return render_template('api_usage.html')


@app.route("/api/get-clean-image/", methods=['GET'])
def get_clean_image():
    output = generate_image(noisy=False)
    return Response(output.getvalue(), mimetype="image/png")


@app.route("/api/get-noisy-image/", methods=['GET'])
def get_noisy_image():
    output = generate_image(noisy=True)
    return Response(output.getvalue(), mimetype="image/png")


def generate_image(noisy: bool = False):
    params = {
        'size_x': 'length',
        'size_y': 'height',
        'style_code': 'style',
        'iter': 'iter'
    }
    for key, value in params.items():
        try:
            params[key] = int(request.args.get(value))
        except (TypeError, ValueError):
            if key in ['size_x', 'size_y']:
                params[key] = 500
            elif key == 'iter':
                params[key] = 200
            else:
                params[key] = None

    img = images.get_image(size_x=params['size_x'], size_y=params['size_y'], style_code=params['style_code'],
                           noisy=noisy, iter=params['iter'])
    return img


if __name__ == '__main__':
    app.run(port=5055, host='0.0.0.0', debug=False)
