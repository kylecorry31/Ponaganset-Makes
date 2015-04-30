<!doctype html>
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <script src="https://code.jquery.com/jquery-1.11.2.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">


    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>

    <script>
        $(function () {
            $('form').submit(function () {
                $.ajax({
                    type: 'POST',
                    url: 'command.php',
                    data: $(this).serialize()
                });
                $('form').clear();
                return false;
            });
        })
    </script>
    <style>
        .jumbotron {
            background-color: #f44336;
            color: white;
            padding: 10rem;
        }
        
        .navbar-brand {
            position: absolute;
            width: 100%;
            left: 0;
            text-align: center;
            margin: auto;
        }
    </style>
</head>

<body>
    <div class="jumbotron">
        <h1 class="text-center">Raspberry Pi</h1>
    </div>

    <div class="container">
        <form>
            <div class="form-group">
                <h1 class="text-center">Command</h1>
                <select name="command" class="form-control">
                    <option value="drive">Drive</option>
                    <option value="morse">Morse</option>
                    <option value="sense">Light Sensor</option>
                    <option value="shutdown">Shutdown</option>
                </select>
            </div>
            <br>
            <br>
            <div class="form-group">
                <h2 class="text-center">Text</h2>
                <input type="text" name="text" class="form-control">
            </div>
            <br>
            <br>
            <center>
                <button type="submit" class="btn btn-primary btn-lg btn-block">Submit</button>
            </center>
        </form>
    </div>

    <nav class="navbar navbar-default navbar-fixed-bottom">
        <div class="container">
            <div class="navbar-header text-center">
                <p class="navbar-brand text-center">Kyle Corry</p>
            </div>
        </div>
    </nav>
</body>

</html>