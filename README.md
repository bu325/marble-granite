# Marble and Granite Management App

This is an offline-first Android application developed with Python (Kivy/KivyMD) for managing a marble and granite supply and installation company.

## Project Structure

```
app/
  main.py
  app.kv
  core/
    i18n.py
    rtl.py
    utils.py
    theme.py
  models/
    __init__.py
    base.py
    inventory.py
    clients.py
    workers.py
    invoices.py
    expenses.py
  services/
    db.py
    pdf.py
    sync.py
    notify.py
    storage.py
    calc.py
  screens/
    __init__.py
    inventory.py
    clients.py
    workers.py
    expenses.py
    invoices.py
    reports.py
    settings.py
    components/                 # Shared UI elements
  widgets/                      # Shared Widgets
  assets/
    fonts/ (Amiri, Cairo)
    icons/
    images/
  tests/
    test_calc.py
    test_models.py
buildozer.spec
README.md
```

## Local Setup and Running

1.  **Install Python 3.11+ and Git.**

2.  **Create a virtual environment and install dependencies:**

    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
    pip install kivy kivymd peewee reportlab arabic_reshaper python-bidi requests plyer matplotlib pillow
    # Note: kivy_garden.matplotlib is for Android build, not typically needed for local desktop run
    ```

3.  **Download and place fonts:**
    Download `Amiri-Regular.ttf` and `Amiri-Bold.ttf` (or Cairo fonts) and place them in `app/assets/fonts/`.

4.  **Run the application:**

    ```bash
    python app/main.py
    ```

## Building APK (Debug & Release)

This project uses `buildozer` to package the Kivy application into an Android APK.

1.  **Install Buildozer:**

    ```bash
    pip install buildozer
    ```

2.  **Initialize Buildozer (if not already done - `buildozer.spec` is provided):**

    ```bash
    buildozer init
    ```

3.  **Build Debug APK:**

    ```bash
    buildozer -v android debug
    ```
    The APK will be generated in the `bin/` directory.

4.  **Build Signed Release APK:**

    a.  **Generate a Keystore (if you don't have one):**

        ```bash
        keytool -genkey -v -keystore my-release-key.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
        ```
        Follow the prompts to set passwords and provide information.

    b.  **Update `buildozer.spec`:**
        Uncomment and fill in the `android.release_keystore`, `android.release_keystore_password`, `android.release_key_alias`, and `android.release_key_password` fields in `buildozer.spec` with your keystore details.

    c.  **Build Release APK:**

        ```bash
        buildozer android release
        ```
        The signed APK/AAB will be in the `bin/` directory.

## Important Notes

*   **RTL Support:** The application is designed with full Right-to-Left (RTL) support for Arabic text. Ensure your system locale supports Arabic for proper display during local development.
*   **Fonts:** Make sure to place the specified Arabic fonts (`Amiri` or `Cairo`) in `app/assets/fonts/` for correct rendering in the app and generated PDFs.
*   **Synchronization:** The synchronization feature (`services/sync.py`) is a placeholder and requires a backend API (e.g., FastAPI, Supabase) to be implemented and configured (`SYNC_API_BASE_URL`).
*   **Test Data:** The application currently does not include a mechanism to generate the specified test data automatically. This would need to be implemented or manually inserted into the SQLite database for testing purposes.


