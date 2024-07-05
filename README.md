# Python CLI Utility PoC for create your own structure and handle dynamically there `command` mapping with Router `function's`

### Testing Via Entry Point Class `main.py`:

    cmd:\> python main.py --router order --command create_order --json_data "{\"product\": \"Laptop\", \"quantity\": 1}" 
    
        Result: {'message': 'Order created for 1 Laptop(s)'}

### Testing Via Object Reference:

    cmd:\> python test_main_object_reference_example_01.py

### Testing Via Subprocess:

    cmd:\> test_app_plugin_subprocess_example_02.py
