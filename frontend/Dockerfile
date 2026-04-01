FROM nginx:alpine

# remove default nginx files
RUN rm -rf /usr/share/nginx/html/*

# copy your frontend files
COPY . /usr/share/nginx/html

# expose port
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]