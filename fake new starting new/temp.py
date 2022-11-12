 encode1 = tf.nn.l2_normalize(embed(tf.constant(text.tolist())), axis=1)
encode2=tf.nn.l2_normalize(embed(tf.constant(text.tolist())), axis=1)