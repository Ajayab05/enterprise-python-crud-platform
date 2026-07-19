FROM nginx:1.27-alpine

# Create writable runtime directories
RUN mkdir -p \
    /tmp/nginx/client_temp \
    /tmp/nginx/proxy_temp \
    /tmp/nginx/fastcgi_temp \
    /tmp/nginx/scgi_temp \
    /tmp/nginx/uwsgi_temp \
 && chown -R 101:101 /tmp/nginx \
 && chown -R 101:101 /usr/share/nginx/html

# Replace nginx configs
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy frontend
COPY index.html /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/

USER 101

EXPOSE 8080

CMD ["nginx","-g","daemon off;"]