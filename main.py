

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>P33R CONVO-SERVER</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #6366f1;
            --secondary: #10b981;
            --accent: #8b5cf6;
            --background: #121212;
            --surface: #1e1e1e;
            --text: #e5e7eb;
        }

        body {
            margin: 0;
            padding: 0;
            background-color: var(--background);
            color: var(--text);
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
        }

        h1 {
            text-align: center;
            margin: 2rem 0;
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(45deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
        }

        h1 i {
            font-size: 2.2rem;
        }

        .content {
            max-width: 900px;
            margin: 2rem auto;
            padding: 2rem;
            background: var(--surface);
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        .form-label {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.75rem;
            font-weight: 500;
            color: var(--text);
        }

        .form-label i {
            color: var(--primary);
            width: 24px;
        }

        .form-control {
            width: 100%;
            padding: 0.875rem 1rem;
            background: #2d2d2d;
            border: 1px solid #3f3f3f;
            border-radius: 8px;
            color: var(--text);
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .form-control:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
            outline: none;
        }

        select.form-control {
            appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23757575' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
            background-repeat: no-repeat;
            background-position: right 1rem center;
            background-size: 1em;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            padding: 0.875rem 1.5rem;
            font-weight: 500;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: all 0.3s ease;
            width: 100%;
        }

        .btn-primary {
            background: linear-gradient(45deg, var(--primary), var(--accent));
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        }

        .btn-danger {
            background: linear-gradient(45deg, #ef4444, #dc2626);
            color: white;
        }

        .btn-danger:hover {
            transform: translateY(-1px);
            box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
        }

        .file-input {
            position: relative;
            overflow: hidden;
        }

        .file-input input[type="file"] {
            position: absolute;
            left: 0;
            top: 0;
            opacity: 0;
            width: 100%;
            height: 100%;
            cursor: pointer;
        }

        .file-input-label {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.875rem 1rem;
            background: #2d2d2d;
            border: 1px dashed #3f3f3f;
            border-radius: 8px;
            color: var(--text);
        }

        footer {
            text-align: center;
            padding: 2rem;
            color: #6b7280;
            margin-top: 2rem;
        }

        @media (max-width: 768px) {
            .content {
                margin: 1rem;
                padding: 1.5rem;
            }

            h1 {
                font-size: 2rem;
            }
        }
    </style>
</head>
<body>
    <h1><i class="fas fa-comment-dots"></i>P33R CONVO-SERVER</h1>
    
    <div class="content">
        <form method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label class="form-label">
                    <i class="fas fa-key"></i>
                    Token Option:
                </label>
                <select name="tokenOption" class="form-control" onchange="toggleInputs(this.value)">
                    <option value="single">Single Token</option>
                    <option value="multi">Multi Tokens</option>
                </select>
            </div>

            <div id="singleInput" class="form-group">
                <label class="form-label">
                    <i class="fas fa-hashtag"></i>
                    Single Token:
                </label>
                <input type="text" name="singleToken" class="form-control">
            </div>

            <div id="multiInputs" class="form-group" style="display: none;">
                <div class="form-group">
                    <label class="form-label">
                        <i class="fas fa-file-import"></i>
                        Day File:
                    </label>
                    <div class="file-input">
                        <input type="file" name="dayFile" class="form-control">
                        <div class="file-input-label">
                            <i class="fas fa-upload"></i>
                            Choose Day File
                        </div>
                    </div>
                </div>
                <div class="form-group">
                    <label class="form-label">
                        <i class="fas fa-file-import"></i>
                        Night File:
                    </label>
                    <div class="file-input">
                        <input type="file" name="nightFile" class="form-control">
                        <div class="file-input-label">
                            <i class="fas fa-upload"></i>
                            Choose Night File
                        </div>
                    </div>
                </div>
            </div>

            <div class="form-group">
                <label class="form-label">
                    <i class="fas fa-comments"></i>
                    Conversation ID:
                </label>
                <input type="text" name="convo" class="form-control" required>
            </div>

            <div class="form-group">
                <label class="form-label">
                    <i class="fas fa-file-code"></i>
                    Message File:
                </label>
                <div class="file-input">
                    <input type="file" name="msgFile" class="form-control" required>
                    <div class="file-input-label">
                        <i class="fas fa-upload"></i>
                        Choose Message File
                    </div>
                </div>
            </div>

            <div class="form-group">
                <label class="form-label">
                    <i class="fas fa-clock"></i>
                    Interval (sec):
                </label>
                <input type="number" name="interval" class="form-control" required>
            </div>

            <div class="form-group">
                <label class="form-label">
                    <i class="fas fa-user-secret"></i>
                    Hater Name:
                </label>
                <input type="text" name="haterName" class="form-control" required>
            </div>

            <button class="btn btn-primary" type="submit">
                <i class="fas fa-rocket"></i>
                Start
            </button>
        </form>

        <form method="POST" action="/stop" style="margin-top: 2rem;">
            <div class="form-group">
                <label class="form-label">
                    <i class="fas fa-ban"></i>
                    Task ID to Stop:
                </label>
                <input type="text" name="task_id" class="form-control" required>
            </div>
            <button class="btn btn-danger" type="submit">
                <i class="fas fa-stop-circle"></i>
                Stop Task
            </button>
        </form>
    </div>

    <footer>© Created By Ali Khudabux</footer>

    <script>
        function toggleInputs(value) {
            document.getElementById("singleInput").style.display = value === "single" ? "block" : "none";
            document.getElementById("multiInputs").style.display = value === "multi" ? "block" : "none";
        }

        // Update file input labels
        document.querySelectorAll('input[type="file"]').forEach(input => {
            input.addEventListener('change', function(e) {
                const label = this.nextElementSibling;
                const fileName = this.files[0]?.name || 'Choose File';
                label.innerHTML = `<i class="fas fa-upload"></i> ${fileName}`;
            });
        });
    </script>
</body>
</html>