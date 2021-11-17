import requests
import datetime

def post_log(step, 
            max_step_size, 
            learning_rate, 
            steps_per_sec,
            localization_loss,
            classification_loss,
            regularization_loss,
            total_loss,
            training_id = None,
            time_stamp = str(datetime.date.today())):

    training_data = {"step": step, 
                     "time_stamp": time_stamp, 
                     "max_step_size": max_step_size, 
                     "learning_rate": learning_rate, 
                     "steps_per_sec": steps_per_sec, 
                     "localization_loss": localization_loss, 
                     "classification_loss": classification_loss, 
                     "regularization_loss": regularization_loss, 
                     "total_loss": total_loss
                    }

    if training_id == None:

        ret_json = requests.post("http://127.0.0.1:8000/training_log_api/", json=training_data)
        return ret_json.json()["training_id"]

    else:
        training_data["training_id"] = training_id
        requests.post("http://127.0.0.1:8000/training_log_api/", json=training_data)

"""

EXAMPLE:

new log that returns uuid
new_uuid = post_log(123, 
            234, 
            0.1, 
            0.4927,
            0.1,
            0.319,
            0.3975,
            0.9)

using old log, post another log with current uuid
post_log(85794, 
        482, 
        0.1, 
        0.4927,
        0.1,
        0.319,
        0.3975,
        0.9,
        training_id = new_uuid)

"""    


