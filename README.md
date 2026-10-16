# Salon Appointment Booking System — Web Technologies Practical Pack

This practice pack covers AngularJS, ReactJS, HTML5, CSS3 animations, JavaScript, Node.js, Express, MongoDB CRUD, XML, internal/external DTD, XSLT sorting, Selenium WebDriver, manual test cases, SQL CRUD alternative, and a Figma quick guide.

## Main app (AngularJS + Express + MongoDB)

Requirements: Node.js 18+ and a reachable MongoDB instance (local MongoDB or Atlas).

1. Copy `.env.example` to `.env`.
2. Set `MONGODB_URI` to your own connection string and optionally set `DB_NAME=salonDB` and `PORT=3000`.
3. Run `npm install`.
4. Run `npm start`.
5. Open http://localhost:3000.

Do not share `.env` or commit database credentials. If port 3000 is busy, stop the old Node server or set `PORT=3001` in `.env` and open http://localhost:3001.

The app has AngularJS data binding, dependency injection, a service, gender filtering, form validation, Express REST routes, and MongoDB create/read/update/delete. Cancellation deletes the appointment after calculating a sample cancellation charge (10% of service price). This is an educational demo policy, not a real salon policy.

## ReactJS demo

Open http://localhost:3000/react.html while the server is running. It demonstrates React components, props, `useState`, form events, and list rendering. It uses CDN scripts and therefore needs internet access. The React demo keeps state in the browser and does not save to MongoDB; the main database-connected application is the AngularJS version.

## XML and XSLT

Files are in `xml/`:
- `appointments.xml` — sample data and XSLT reference.
- `appointments.xsl` — transforms XML into a table and sorts by customer name.
- `appointments-internal-dtd.xml` — internal DTD example.
- `appointments-external-dtd.xml` and `appointments.dtd` — external DTD example.

Open the XML/XSLT file in a browser that supports local XSLT. If browser security or local-file restrictions prevent the transform, use an XML editor or run a local XML/XSLT processor.

## Selenium WebDriver (Python)

1. Install Python and Chrome.
2. Install Selenium: `python -m pip install selenium`.
3. From the project root, run `python testing/test_login.py`.
4. Chrome opens `testing/selenium_demo.html`. Manually enter credentials and click Login, then return to the terminal and press Enter so Selenium verifies the displayed result. Demo credentials are `admin` / `12345`.

Selenium Manager normally handles the browser driver automatically. The first run may need internet access to obtain a compatible driver.

## MySQL alternative

`sql/salon_schema.sql` contains table creation, sample inserts, SELECT, UPDATE, and DELETE examples. Run it in MySQL Workbench or a MySQL terminal. This is a separate SQL practice alternative; the main app uses MongoDB.

## Figma

See `figma-practice.md` for a short wireframe/prototype exercise.

## Notes

- This is a learning project, not production software. Authentication, privacy controls, payment processing, appointment-slot conflict prevention, and real cancellation policy are not implemented.
- The React demo is separate from the AngularJS CRUD app.
- Always test with your own database connection; generating project files alone does not prove a live database connection works.
