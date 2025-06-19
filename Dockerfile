FROM python:3.11-slim

# COPY requirements.txt /appdata/
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . /appdata/
# RUN chmod +x /appdata/entrypoint.sh
# ENTRYPOINT ["/appdata/entrypoint.sh"]


WORKDIR /appdata
COPY . /appdata/

# RUN pip install selenium pytest pytest-xdist webdriver-manager
RUN pip install -r requirements.txt

# CMD ["pytest", "-n", "auto", "--dist=loadscope", "--maxfail=1", "--tb=short"]
CMD ["pytest", "-n", "3"]

