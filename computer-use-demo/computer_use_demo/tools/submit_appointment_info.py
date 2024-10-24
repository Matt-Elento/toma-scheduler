
from anthropic.types.beta.beta_tool_param import BetaToolParam

from .base import BaseAnthropicTool, ToolResult


class SubmitAppointmentInfoTool(BaseAnthropicTool):
    def __init__(self):
        super().__init__()

    def to_params(self) -> BetaToolParam:
        return {
            "name": "submit_appointment_info",
            "description": (
                "Use immediately only when the appointment is successfully "
                "scheduled and you have an appointment id"
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "appointment_id": {
                        "type": "string",
                        "description": "Appointment id of the scheduled appointment"
                    },
                },
                "required": ["appointment_id"]
            }
        }

    async def __call__(self, **kwargs):
        kwargs_str = str(kwargs)
        return ToolResult(output=kwargs_str)

