from models.answers import answers

questions = [
    {
        "question": "¿Cuál es el costo de asegurar mi envío?",
        "response": answers.cost(),
    },
    {
        "question": "cuanto cuesta?",
        "response": answers.cost(),
    },
    {
        "question": "comprar",
        "response": ["El costo de asegurar tu envío es de $10.000"],
    },
    {
        "question": "¿Cómo puedo verificar el estado de mi envío?",
        "response": [
            "Puedes verificar el estado de tu envío a través de este link: https://estado.link"
        ],
    },
    {
        "question": "estado status",
        "response": [
            "Puedes verificar el estado de tu envío a través de este link: https://estado.link"
        ],
    },
    {
        "question": "¿Cómo puedo hacer el seguimiento está mi envío?",
        "response": [
            "Puedes hacer seguimiento de tu envío a través de este link: https://seguimiento.link"
        ],
    },
    {
        "question": "donde",
        "response": [
            "Puedes hacer seguimiento de tu envío a través de este link: https://seguimiento.link"
        ],
    },
    {
        "question": "¿Cuál es la distancia máxima que hacen?",
        "response": answers.distance(),
    },
    {
        "question": "distancia, kms",
        "response": answers.distance(),
    },
    {
        "question": "hasta donde lo llevan",
        "response": answers.distance(),
    },
    {
        "question": "¿Me puedes pasar un número de soporte?",
        "response": answers.contact_number(),
    },
    {
        "question": "num, numero",
        "response": answers.contact_number(),
    },
    {
        "question": "¿Qué tipo de vehículos utilizan?",
        "response": [
            "En Xegure utilizamos camionetas, furgonetas, autos y camiones blindados"
        ],
    },
    {
        "question": "¿Qué tipo de camionetas usan?",
        "response": answers.kind_of_vans(),
    },
    {
        "question": "Hola",
        "response": answers.hello(),
    },
    {
        "question": "Hola, buenas tardes",
        "response": answers.hello(),
    },
    {
        "question": "¿Cómo te llamas?",
        "response": answers.what_is_your_name(),
    },
    {
        "question": "¿Cómo estás?",
        "response": ["Estoy bien, ¡muchas gracias! ¿En qué puedo ayudarte?"],
    },
    {
        "question": "Hola, ¿cómo estás?",
        "response": answers.hello_how_are_you(),
    },
    {
        "question": "Quisiera hacerte una consulta",
        "response": [
            "¡Por supuesto! Estoy aquí para ayudarte con cualquier consulta que tengas sobre Xegure."
        ],
    },
    {
        "question": "Necesito ayuda",
        "response": ["Muy bien, ¿en qué puedo ayudarte?"],
    },
    {
        "question": "¡Adiós!",
        "response": answers.goodbye(),
    },
    {
        "question": "Muchas gracias, muchísimas gracias, has sido de mucha ayuda.",
        "response": answers.thank_you(),
    },
]
