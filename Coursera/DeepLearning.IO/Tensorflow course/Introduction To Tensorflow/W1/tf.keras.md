### Module: tf.keras.Model
A model grouping layers into an object with training/inference features.
Inherits From: [`Layer`], [`Module`]
```
tf.keras.Model(    *args, **kwargs)
```
	

### Module: tf.keras.activations
$I- Functions:$
	 1. deserialize(...): Returns activation function given a string identifier.
		 ***`tf.keras.activations.deserialize(name, custom_objects=None, use_legacy_format=False)`***
		- name: The name of the activation function.
		- custom_objects: Optional {function_name: function_obj} dictionary listing user-provided activation functions.
		- use_legacy_format: Boolean, whether to use the legacy format for deserialization. Defaults to False.
		- returns: Corresponding activation function.
	2. elu(...): Exponential Linear Unit.
		```tf.keras.activations.elu(    x, alpha=1.0)```
		The exponential linear unit (ELU) with `alpha > 0` is: `x` if `x > 0` and `alpha * (exp(x) - 1)` if `x < 0` The ELU hyperparameter `alpha` controls the value to which an ELU saturates for negative net inputs. ELUs diminish the vanishing gradient effect.
		ELUs have negative values which pushes the mean of the activations closer to zero. Mean activations that are closer to zero enable faster learning as they bring the gradient closer to the natural gradient. ELUs saturate to a negative value when the argument gets smaller. Saturation means a small derivative which decreases the variation and the information that is propagated to the next layer.
				
