Define Requirements:

Database System:
MySQL because it is simple and easy to use

Forms:
  Registration/liberacion de repsonsabilidad(llenado por los papas):
    name  *
    birth_date  *
    weight *
    height *
    disability *
    school/institucion *
    teacher *
    nombre_tutor *
    que es del paceinte el tutor *
    calle y Nº *
    ciudad y estado *
    codigo postal *
    telefono_domicilio *
    telefono_celular *
    telefono_adicional *(Registre otro número telefónico en el cual se pueda contactar a algún responsable del participantes e indique una descripción, por ejemplo, trabajo, familiar, etc.
    )
    correo *
    uso de fotografia? *
    archivo con firma digitalizada para autorizar lo de las fotos
    Liberacion de responsabilidad:
      '''Conozco el potencial de
      riesgo que surge de la equitación y en general del riesgo de las actividades
      ecuestres, incluyendo lesiones corporales graves. Sin embargo, estoy consciente
      que los beneficios para el  participante
      son mayores que el riesgo que se asume. Con la intención de quedar vinculado
      legalmente por mí, mis herederos, cesionarios y administradores, libero para
      siempre de todas las reclamaciones por daños y perjuicios contra Amigos de Riendas
      para la Vida AC y sus instructores, terapistas, empleados, voluntarios,
      caballos y cualquier otra persona relacionada con el programa, por cualquier lesión
      y / o pérdidas que el participante pudiera sufrir durante su permanencia en el
      programa por cualquier causa, incluyendo si existiese negligencia de las partes
      liberadas.



      El abajo firmante reconoce
      que él/ella ha leído este Formato de Registro y Liberación en su totalidad; que
      él/ella comprende los términos de esta liberación y ha firmado este formato
      voluntariamente y con pleno conocimiento de sus efectos.``````
      fecha
      fecha,
      nombre
      firma (file)
    medico *
    clinica y hospital de preferencia *
    compañia de seguro *
    poliza No *
    Alergias, medicamentos y otros aspectos de salud a tomar en cuenta *
      En caso de no presentar condiciones relevantes, favor responder "No aplica" 
    contacto de emergencia 1*
    contancto de emergencia 2*

    **esta parte estam uy confusa, checala en https://docs.google.com/forms/d/e/1FAIpQLSdxNFGosR98WbtfqYNrhst4wMuQtoQ9v2e0ubOABNMQPZo2bQ/formResponse
    doy constemimiento?
      si (redicciona a otra pagina)
      no (redicciona a otra pagina)
    sindrome de down?
      ¿Presenta Síntomas Neurológicos de Inestabilidad Atlantoaxial (Indique los síntomas)?

    

  Datos_generales (llenado por instructoras)
    name
    birth_date
    contact_cel
    diagnosis


Platform for app development: 
Progressive web app is the choice because:
  -works on any type of device (phones, desktops, etc) because there are no platform specific development
  -installation not required because it is accesible through URL
  -A single codebase serves all user (one platform)
  -Can work offline or with poor internet connection
  -engagement with distinct features
  -Discoverable (idk about that one for this case)
  -Update simplicity because it updates when refreshing the page
  -Served over HTTPS
  -Responsive Designs
  -User analytics
  -Lower data usage
  -no app store feed




Design the Database Schema:

Plan the structure of your database. Decide what tables you need, the fields in each table, and the relationships between them.

Registration table:
id AUTOINCREMENT PRIMARY (for tracking the id of each child, in case two children have the same name, this will make them different to the server)
name 
contact phone
Diagnostico ( motriz, neurologico, conductual, lenguaje, social, otros)






Design the User Interface:

Design the forms for data entry. Make sure the interface is user-friendly and mobile-responsive.
Backend Development:

Develop the server-side logic to handle form submissions and interact with the database.
Choose a programming language (e.g., Node.js, Python, Ruby) for your backend.
Implement APIs to send and receive data from the mobile app.
Frontend Development:

Build the mobile app's user interface.
Implement functionality to send data to the server when a form is submitted.
Security:

Implement proper security measures, including user authentication, to protect user data.
Testing:

Thoroughly test your app to ensure it works correctly, handles errors, and is user-friendly.
Deployment:

Deploy your backend to a server or cloud platform.
Publish your mobile app to the App Store (iOS) or Google Play (Android).
User Feedback and Improvements:

Gather user feedback and make improvements to your app.
Scaling:

Prepare for scaling as your user base grows. Optimize your database and server infrastructure for performance.
Maintenance:

Regularly maintain your app to fix bugs, update libraries, and add new features.
Legal Considerations:

Be aware of data protection and privacy laws that may apply to the data you're collecting.
Documentation:

Document your database schema, API endpoints, and codebase for future reference.



## Registration Form

    Nombre del Paciente:
    Edad del Paciente:
    Diagnostico:
      Motriz
      Social
      Lenguaje
      Neurologico
      Conductual
      Otro : Especificar
    Tutor 1 del Paciente: *Obligatorio
    Tutor 2 del Paciente: *Opcional
    Telefono de contacto: *Obligatorio
    2 telefono de contacto: *Opcional

   
