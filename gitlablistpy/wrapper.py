import os
import gitlab


class GitlabWrapper:
    gl = None

    @classmethod
    def get(cls):
        if cls.gl:
            return cls.gl

        url = os.environ['GITLAB_URL']
        if not url:
            raise Exception('GITLAB_URL env var not set')
        token = os.environ['GITLAB_API_TOKEN']
        if not token:
            raise Exception('GITLAB_API_TOKEN env var not set')
        gl = gitlab.Gitlab(url, token)
        gl.auth()
        cls.gl = gl
        return gl
