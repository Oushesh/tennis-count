## History

## Presentation of different methodologies

## Comparison and why?
   * It seems currently there has been a huge change in the world of detection. Segmentation started with Fully Connected Network. Detection started with Faster-RCNN --> SSD --> YOLO --> MaskRCNN --> Optimisation of the loss functions from normal loss to Focal Loss to Retina Loss

   Normal Loss Function in a detector is: CE: Categorical Cross_Entropy.
   * CE  = -log(p_t) if y=1 else -log(1-p_t) (if y=0)
   * The incoming Focal Loss Function is:
     FL(p_t) = -alpha_t*(1-p_t)*exp(gamma)*log(p_t)

     The effect of having the alpha and exp(gamma) is to cater for imbalancement.
     https://amaarora.github.io/2020/06/29/FocalLoss.html


  * Even when  I was writing my thesis: We  had to use Feature Vectors
      then pass to a series of LSTM - Bi-LSTM to translate the feature
      vectors then learn a Se2Seq model.

  * Now with the Transformers its possible to perform detection in parallel and fast
      to the speed of classification.

  * DETR: direct set prediction problem. Transformers use attention mechanisms.
     (Attentions is all you need.)

  + Everything that is a sequence can be modeled with the transformer:
       https://medium.com/the-dl/transformers-from-scratch-in-pytorch-8777e346ca51#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjZhOGJhNTY1MmE3MDQ0MTIxZDRmZWRhYzhmMTRkMTRjNTRlNDg5NWIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2MTY0OTMxNTYsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwMTc0ODUzNDQyMjEwMDA5NTc2MiIsImVtYWlsIjoib3VzaGVzaEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6Ik91c2hlc2ggSGFyYWRodW4iLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2c3ZkktS1dkMTlTamh0WUlGdjZjZDNpUXpLak13ZGZmS3kxZUx5cnc9czk2LWMiLCJnaXZlbl9uYW1lIjoiT3VzaGVzaCIsImZhbWlseV9uYW1lIjoiSGFyYWRodW4iLCJpYXQiOjE2MTY0OTM0NTYsImV4cCI6MTYxNjQ5NzA1NiwianRpIjoiODNlMDA3YzdjM2JkNWI0NGY4Y2FjNzQzMzA5NzU1YjdkNmM0YjBmMiJ9.j2ewajXFS-2AKE2MdKcqTHWCs4bn1XUqfN4xqv1KYVFo7kVVpguyDtjH9195fkhWljvx-lMa0nO3FqoyuAAfIKAvObOhgQxOq_jNux0cXXoNorLB01gvfprYfe-KxNZxpU5pfeuWgTWy2AfAkJfSLLerR85y2FmhiM1C-plfTYOV2u4om7xm832cyr6szo45cA8znfzgYQzJ3Bhih1Cb7a6JjHClH4gJ1X2RIbHAvJqBlM-sw_q6OXCEZZQMUgzRkUyb83LLHoo-CSJMUPtp3RaieoIUmyOTjHpjpeEj0TY6tCIAipT4NmX_vMzxhCbOjl1B3Z_DAIBCFyKXd5SpYw

  * To test the code and bring it for my own project for scene understanding in VR.


  * 
